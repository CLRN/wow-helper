from machines.mob_farmer import MobFarmer

from unittest.mock import Mock, call


def test_farm():
    window = Mock()
    object_manager = Mock()
    combat_model = Mock()
    controller = Mock()
    mob_picker = Mock()

    machine = MobFarmer(window=window,
                        controller=controller,
                        object_manager=object_manager,
                        combat_model=combat_model,
                        mob_picker=mob_picker,
                        telegram_bot=None)
    assert machine.is_restoring



