import daft
import itertools

import shared.src.utils.util as shared_util

def make_mixture_plate_graph(group_observed=True):
    group = daft.Node("$g$", "$g$", x=3, y=6, observed=group_observed, scale=3)
    observed = daft.Node("$x$", "$x$", x=6, y=6, observed=True, scale=3)
    group_params = daft.Node("$\lambda$", "$\lambda$", x=3, y=3, scale=3)
    shared_param = daft.Node("$\\beta$", "$\\beta$", x=4.5, y=9, scale=3)

    nodes = [group, observed, group_params, shared_param]
    edges = [("$g$", "$x$"), ("$\lambda$", "$x$"), ("$\\beta$", "$x$")]

    graph = daft.PGM(shape=(9, 12), label_params={"fontsize": "xx-large"})

    within_group_plate = daft.Plate([1.5, 4.5, 6, 3], label="$N$", position="bottom right", rect_params={"lw": 2})
    between_group_plate = daft.Plate([1, 1, 7, 7], label="$K$", position="bottom right", rect_params={"lw": 2})

    plates = [within_group_plate, between_group_plate]

    [graph.add_node(node) for node in nodes]
    [graph.add_edge(*edge, head_width=0.5, lw=4) for edge in edges]
    [graph.add_plate(plate) for plate in plates]

    shared_util.clean_plates(graph)

    graph.render();

def make_mixture_plateless_graph():
    obs = [1, 2, 3]
    groups = [1, 2]
    group_nodes = [daft.Node(f"$g_{i}$", f"$g_{i}$", x=3, y=3.5 * i, observed=True, scale=3)
                   for i in obs]
    observed_nodes = [daft.Node(f"$x_{i}$", f"$x_{i}$", x=6, y=3.5 * i, observed=True, scale=3)
                      for i in obs]
    group_params = [daft.Node(f"$\lambda_{k}$", f"$\lambda_{k}$", x=8, y=4 + 2 * k, scale=2.5)
                    for k in groups]
    shared_param = daft.Node("$\\beta$", "$\\beta$", x=12, y=7, scale=3)

    nodes = group_nodes + observed_nodes + group_params + [shared_param]

    observation_edges = [(f"$g_{i}$", f"$x_{i}$") for i in obs]
    group_param_edges = [(f"$\lambda_{k}$", f"$x_{i}$") for i, k in itertools.product(obs, groups)]
    shared_param_edges = [("$\\beta$", f"$x_{i}$") for i in obs]

    edges = observation_edges + group_param_edges + shared_param_edges

    graph = daft.PGM(shape=(15, 12), label_params={"fontsize": "xx-large"})

    [graph.add_node(node) for node in nodes]
    [graph.add_edge(*edge, head_width=0.5, lw=4) for edge in edges]

    graph.render();