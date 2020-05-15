# Player class


class Player:

    def __init__(self,
                 hp,
                 head_slots,
                 arm_slots,
                 body_slots,
                 leg_slots,
                 power):

        self.base_hp = hp

        self.current_hp = hp

        self.energy = 3

        self.armor = 0

        self.head_slots = head_slots

        self.arm_slots = arm_slots

        self.body_slots = body_slots

        self.leg_slots = leg_slots

        self.power = power
