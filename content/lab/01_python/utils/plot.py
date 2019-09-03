import matplotlib.pyplot as plt

def temp_over_time(data, name="Ohio Street"):
    """Plots the water_temp and time columns of the dataframe data
    for rows whose name column matches the argument name.
    """
    for column in ["name", "water_temp", "time"]:
        if column not in data.columns:
            raise AttributeError(f"dataframe does not contain column '{column}'")

    name_selector = data.name == name
    f, ax = plt.subplots(figsize=(16, 4))

    ax.scatter(list(data[name_selector]["time"]), data[name_selector]["water_temp"], alpha=0.05);
    ax.set_ylabel("water_temp"); ax.set_xlabel("time")
    plt.title(f"Temperature at {name}")
