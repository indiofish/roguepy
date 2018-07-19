def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    entity.combat.heal(amount)
    results.append({'item_used': True, 'msg': "Healed!"})

    return results
