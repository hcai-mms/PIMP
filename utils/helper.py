import dash_bootstrap_components as dbc


def make_toast(message, id_):
    """
    Helper function for making a toast. dict id for use in pattern matching
    callbacks.
    """
    return dbc.Toast(
        message,
        id={"type": "toast", "id": id_},
        key=id_,
        header="Notice",
        is_open=True,
        dismissable=True,
        icon="danger",
    )