def get_technology(table: str, technology: str):
    technology = technology if technology else table.split("_")[-3]
    return technology


def get_model(table: str, model: str = None):
    model = model if model else table.split("_")[-1]
    return model
