import daft

def display_mdma_model():
    s, asp = 3, 1.25
    
    dose_node = daft.Node("dose", "MDMA\nDose", 1, 3, scale=s, aspect=asp)
    social_node = daft.Node("social_setting", "Social\nSetting", 1, 1, scale=s, aspect=asp)

    esteem_node = daft.Node("esteem", "Self\nEsteem", 5, 3, scale=s, aspect=asp)
    mood_node = daft.Node("mood", "Mood", 5, 1, scale=s, aspect=asp)

    mdma_model = daft.PGM([7, 4], line_width=4, label_params={"fontsize": 16, "fontweight": "bold"})
    
    nodes = [dose_node, social_node, esteem_node, mood_node]
    edges = [("dose", "esteem"), ("dose", "mood"),
             ("social_setting", "esteem"), ("social_setting", "mood")]
    
    [mdma_model.add_node(node) for node in nodes]
    [mdma_model.add_edge(*edge) for edge in edges]

    mdma_model.render();
    
def display_huth_model():
    s, asp = 3, 1.25
    empty_params = {"linewidth": 0}
    
    semantic_node = daft.Node("semantic", "Semantic\nContent", 1, 3, scale=s, aspect=asp)
    
    voxel1_node = daft.Node("voxel1", "voxel1", 5, 5, scale=s, aspect=asp)
    
    empty1_node = daft.Node("empty1", "", 5, 4, scale=s, aspect=asp, plot_params=empty_params)
    ellipsis = daft.Node("ellipsis", "...", 5, 3, scale=s, aspect=asp, plot_params=empty_params)
    emptyN_node = daft.Node("emptyN", "", 5, 2, scale=s, aspect=asp, plot_params=empty_params)
    
    voxelN_node = daft.Node("voxelN", "voxelN", 5, 1, scale=s, aspect=asp)

    huth_model = daft.PGM([7, 6], line_width=4, label_params={"fontsize": 16, "fontweight": "bold"})

    
    nodes = [voxel1_node, voxelN_node, semantic_node, ellipsis, empty1_node, emptyN_node]
    edges = [("semantic", "voxel1"),
             ("semantic", "empty1"), ("semantic", "ellipsis"), ("semantic", "emptyN"),
             ("semantic", "voxelN")]
    
    [huth_model.add_node(node) for node in nodes]
    [huth_model.add_edge(*edge) for edge in edges]

    huth_model.render();