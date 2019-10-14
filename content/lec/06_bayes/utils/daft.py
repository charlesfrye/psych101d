import daft

import shared.src.utils.util as shared_util


def make_switchpoint_model():
    scale = 2
    p1 = daft.Node("$p_1$", "$p_1$", x=3, y=5.25, scale=scale)
    p2 = daft.Node("$p_2$", "$p_2$", x=5, y=5.25, scale=scale)
    s = daft.Node("$s$", "$s$", x=1.5, y=4, scale=scale)
    p = daft.Node("$p$", "$p$", x=3.5, y=3, scale=scale)
    obs = daft.Node("obs", "obs", x=3.5, y=0.75, observed=True, scale=scale)
    
    plate = daft.Plate((2.5, 0.15, 2, 3.5),label="$N$")

    nodes = [p1, p2, s, p, obs]
    edges = [("$p_1$", "$p$"), ("$p_2$", "$p$"), ("$s$", "$p$"), ("$p$", "obs")]

    pgm = daft.PGM((6, 6))
    [pgm.add_node(node) for node in nodes]
    [pgm.add_edge(*edge, lw=3, head_width=0.3) for edge in edges]
    
    pgm.add_plate(plate)
    shared_util.clean_plates(pgm)
    pgm.render();
    

def make_text_model():
    scale = 2
    alpha = daft.Node("$\lambda$", "$\lambda$",  x=4, y=6.5, scale=scale, observed=True)
    p1 = daft.Node("$\mu_1$", "$\mu_1$", x=3, y=5.25, scale=scale)
    p2 = daft.Node("$\mu_2$", "$\mu_2$", x=5, y=5.25, scale=scale)
    s = daft.Node("$s$", "$s$", x=1.5, y=4, scale=scale)
    p = daft.Node("$\mu$", "$\mu$", x=3.5, y=3, scale=scale)
    obs = daft.Node("obs", "obs", x=3.5, y=0.75, observed=True, scale=scale)
    
    plate = daft.Plate((2.5, 0.15, 2, 3.5),label="$N$")

    nodes = [alpha, p1, p2, s, p, obs]
    edges = [("$\lambda$", "$\mu_1$"), ("$\lambda$", "$\mu_2$"),
        ("$\mu_1$", "$\mu$"), ("$\mu_2$", "$\mu$"),
        ("$s$", "$\mu$"), ("$\mu$", "obs")]

    pgm = daft.PGM((6, 8))
    [pgm.add_node(node) for node in nodes]
    [pgm.add_edge(*edge, lw=3, head_width=0.3) for edge in edges]
    
    pgm.add_plate(plate)
    shared_util.clean_plates(pgm)
    pgm.render();