from model.database import Database

class Model(Database):
    def __init__(self):
        super(Model, self).__init__()

    def get_categories(self):
        conn = self.getConn()
        conn.execute("""
        SELECT * FROM category;
        """)
        rows = conn.fetchall()

        result = []
        for record in rows:
            result.append(dict(record))
        self.commit()
        self.closeConn()
        return result

    def get_questions(self, categoryid, questiontype):

        conn = self.getConn()
        conn.execute("""
        SELECT * FROM question WHERE category_id = %s AND type = %s
        """, (categoryid, questiontype,))

        questionrows = conn.fetchall()
        questionresult = []
        for record in questionrows:
            questionresult.append(dict(record))

        questionids = ()

        for question in questionresult:
            questionids += (question['id'],)

        answers = []
        result = []
        if len(questionids) > 0:
            conn.execute("""
            SELECT * FROM answer WHERE question_id IN %s;
            """, (questionids,))

            answers = conn.fetchall()

        for question in questionresult:
            result.append(question)
            last_append_idx = len(result) - 1
            last_append_question = result[last_append_idx]
            last_append_question['answers'] = []
            for answer in answers:
                if answer['question_id'] == last_append_question['id']:
                    result[last_append_idx]['answers'].append(dict(answer))

        self.commit()
        self.closeConn()

        # print(result[0])
        return result

    def get_highscores(self):
        conn = self.getConn()
        conn.execute("""
        SELECT * FROM highscore ORDER BY score DESC LIMIT 10;
        """)
        rows = conn.fetchall()
        result = []
        for record in rows:
            result.append(dict(record))
        self.commit()
        self.closeConn()
        return result
