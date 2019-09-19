from machines.combat_action import CombatAction
from components.spell import Spell

from unittest.mock import Mock, call

attack_spell = Spell(0, 2, 5, 0, '1', 1)
smite_spell = Spell(0, 2, 25, 2, '2', 0)


def test_smite_simple():
    controller = Mock()

    calls = {"up": list(), "down": list(), "press": list()}

    machine = CombatAction(controller)
    assert machine.is_in_range

    machine.process(30, 0, smite_spell, False)
    assert machine.is_moving_to
    calls['down'].append(call('w'))

    machine.process(24, 0, smite_spell, False)
    assert machine.is_in_range
    calls['up'].append(call('w'))

    machine.process(24, 0, smite_spell, False)
    assert machine.is_casting_started
    calls['press'].append(call(smite_spell.bind_key))

    machine.process(24, 0, smite_spell, True)
    assert machine.is_casting

    machine.process(10, 0, smite_spell, True)
    assert machine.is_casting

    machine.process(1, 0, smite_spell, False)
    calls['down'].append(call('s'))
    assert machine.is_moving_away

    machine.process(4, 0, smite_spell, False)
    calls['up'].append(call('s'))
    assert machine.is_in_range

    machine.process(4, 0, smite_spell, False)
    assert machine.is_casting_started
    calls['press'].append(call(smite_spell.bind_key))

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)


def test_melee_simple():
    controller = Mock()

    calls = {"up": list(), "down": list(), "press": list()}

    machine = CombatAction(controller)
    assert machine.is_in_range

    machine.process(30, 0, attack_spell, False)
    assert machine.is_moving_to
    calls['down'].append(call('w'))

    machine.process(4, 0, attack_spell, False)
    assert machine.is_in_range
    calls['up'].append(call('w'))

    machine.process(4, 0, attack_spell, False)
    assert machine.is_in_range
    calls['press'].append(call(attack_spell.bind_key))

    machine.process(4, 0, attack_spell, False)
    assert machine.is_in_range
    calls['press'].append(call(attack_spell.bind_key))

    machine.process(1, 0, attack_spell, False)
    calls['down'].append(call('s'))
    assert machine.is_moving_away

    machine.process(4, 0, attack_spell, False)
    calls['up'].append(call('s'))
    assert machine.is_in_range

    machine.process(4, 0, attack_spell, False)
    assert machine.is_in_range
    calls['press'].append(call(attack_spell.bind_key))

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)
