def set_direction(self):
    if self.direction == 'left' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'left':
        if self.steps == 3:
            self.tower['tower_id'] = 't3'
            self.tower['current_pos'] = "right"
        if self.steps == 2:
            self.tower['tower_id'] = 't4'
            self.tower['current_pos'] = "left"
        if self.steps == 1:
            self.tower['tower_id'] = 't4'
            self.tower['current_pos'] = 'right'

    elif self.direction == 'right' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'left':
        print('drig')
        if self.steps == 3:
            print('in3')
            self.tower['tower_id'] = 't2'
            self.tower['current_pos'] = "right"
        if self.steps == 2:
            print('in2')
            self.tower['tower_id'] = 't2'
            self.tower['current_pos'] = "left"
        if self.steps == 1:
            print('in1')
            self.tower['tower_id'] = 't1'
            self.tower['current_pos'] = 'right'

    elif self.direction == 'left' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'right':
        if self.steps == 3:
            self.tower['tower_id'] = 't3'
            self.tower['current_pos'] = "left"
        if self.steps == 2:
            self.tower['tower_id'] = 't4'
            self.tower['current_pos'] = "right"
        if self.steps == 1:
            self.tower['tower_id'] = 't1'
            self.tower['current_pos'] = 'left'

    elif self.direction == 'right' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'right':
        if self.steps == 3:
            self.tower['tower_id'] = 't3'
            self.tower['current_pos'] = "left"
        if self.steps == 2:
            self.tower['tower_id'] = 't2'
            self.tower['current_pos'] = "right"
        if self.steps == 1:
            self.tower['tower_id'] = 't2'
            self.tower['current_pos'] = 'left'

    elif self.direction == 'right' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'middle':
        if self.steps == 3:
            self.tower['tower_id'] = 't4'
        if self.steps == 2:
            self.tower['tower_id'] = 't3'
        if self.steps == 1:
            self.tower['tower_id'] = 't2'

    elif self.direction == 'left' and self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'middle':
        if self.steps == 3:
            self.tower['tower_id'] = 't2'
        if self.steps == 2:
            self.tower['tower_id'] = 't3'
        if self.steps == 1:
            self.tower['tower_id'] = 't4'
