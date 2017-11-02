import rules
import backend.models

@rules.predicate
def is_public_kit(user, kit):
    """
    Predicate defining whether a kit is public or not.
    """
    if not isinstance(kit, backend.models.Kit):
        return False

    return kit.privacy_public_dashboard

@rules.predicate
def is_target(user, obj):
    """
    Predicate defining whether the user is exactly the target object.
    """
    if not user or not obj:
        return False

    return user == obj

@rules.predicate
def is_kit_member(user, kit):
    """
    Predicate defining whether a user is a member of a kit.
    """
    if not user or not isinstance(kit, backend.models.Kit):
        return False

    return len(kit.users.filter(pk=user.pk)) == 1

@rules.predicate
def is_public_sensor_definition(user, sensor_definition):
    """
    Predicate defining whether a sensor definition is public or not.
    """
    if not isinstance(kit, backend.models.SensorDefinition):
        return False

    return sensor_definition.public

@rules.predicate
def is_sensor_definition_owner(user, sensor_definition):
    """
    Predicate defining whether a user is the owner of sensor definition.
    """
    if not user or not isinstance(kit, backend.models.SensorDefinition):
        return False

    return sensor_definition.owner == user

# Permissions
rules.add_perm('backend.view_kit_dashboard', is_public_kit | is_target | is_kit_member)
rules.add_perm('backend.subscribe_to_kit_measurements_websocket', is_public_kit | is_target | is_kit_member)
rules.add_perm('backend.configure_kit', is_kit_member | is_target)
rules.add_perm('backend.view_sensor_definition', is_public_sensor_definition | is_sensor_definition_owner)
rules.add_perm('backend.assign_sensor_definition', is_public_sensor_definition | is_sensor_definition_owner)
rules.add_perm('backend.edit_sensor_definition', is_sensor_definition_owner)
