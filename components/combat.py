class Combat():
    """the combat module for all entities that can combat"""
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, dmg):
        results = []

        self.hp -= dmg

        if self.hp <= 0:
            results.append({'dead': self.owner})
            ret = self.owner.dead()
            results.append({'msg': ret})

        return results


    def attack(self, target):
        results = []
        # TODO: check if target has combat module?
        dmg = self.power - target.combat.defense

        if dmg > 0:
            txt = {'msg': "{0}, attacks {1} for {2} damage.".format(
                self.owner.name, target.name, str(dmg))}
            results.append(txt)
            results.extend(target.combat.take_damage(dmg))
        else:
            txt = {'msg': "no dmg!"}
            results.append(txt)

        return results

    def heal(self, amount):
        # if it exceeds max_hp, then only heal upto max_hp
        self.hp = min(self.hp+amount, self.max_hp)
