from machines.mob_farmer import MobFarmer

from unittest.mock import Mock, call


def test_farm():
    object_manager = Mock()
    combat_model = Mock()
    controller = Mock()
    mob_picker = Mock()

    machine = MobFarmer(controller=controller,
                        object_manager=object_manager,
                        combat_model=combat_model,
                        mob_picker=mob_picker)
    assert machine.is_looting



