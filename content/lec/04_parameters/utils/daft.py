import daft


def make_bivariate_graph(param, obs, observed=False, plate=False, scale=2):
    arrow_params = {"linewidth": 2,
                    "head_width": 0.25}
    if param == "sigma":
        param_string = r"$\sigma$"
    elif param == "mu":
        param_string = r"$\mu$"
    else:
        param_string = param

    param_node = daft.Node("param", param_string, 1, 2.5, scale=scale)
    obs_node = daft.Node("obs", obs, 3.5, 2.5, scale=scale, observed=observed)

    obs_plate = daft.Plate([2.5, 1.5, 2, 2],
                           label=r"$N$", position="bottom right")

    bivariate_model_graph = daft.PGM([5, 5], line_width=2,
                                     label_params={"fontsize": 32})

    bivariate_model_graph.add_node(param_node)
    bivariate_model_graph.add_node(obs_node)

    bivariate_model_graph.add_edge("param", "obs", **arrow_params)

    if plate:
        bivariate_model_graph.add_plate(obs_plate)

        # Avoid fill with blue in newer versions of matplotlib
        bivariate_model_graph._plates[0].bbox["fc"] = "white"

    bivariate_model_graph.render()
    return bivariate_model_graph


def make_parameters_graph(observed=True, plate=False):

    arrow_params = {"linewidth": 2,
                    "head_width": 0.25}

    in_nodes = [daft.Node(
        f"theta_{ii}", f"$\\beta_{ii}$", 1, 4 - 1.5 * ii, scale=2, observed=observed)
                for ii in range(3)]
    x_node = daft.Node("x", "x", 3.5, 2.5, scale=2, observed=False)

    parameters_graph = daft.PGM([5, 5], line_width=2,
                                label_params={"fontsize": 32})

    [parameters_graph.add_node(node) for node in in_nodes]
    parameters_graph.add_node(x_node)

    [parameters_graph.add_edge(f"theta_{ii}", "x", **arrow_params) for ii in range(3)]

    parameters_graph.render()

    return parameters_graph
