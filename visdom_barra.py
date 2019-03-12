import visdom


def gerar_barras(eixo_y: float, eixo_x: float):
    vis = visdom.Visdom()
    vis.bar
    return vis.bar(eixo_y, eixo_x)
