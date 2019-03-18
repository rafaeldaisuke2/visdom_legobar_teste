# bar plots
import visdom
import numpy as np

vis = visdom.Visdom()

vis.close(win=None)
vis.bar(
    X=[1, 2, 3, 4, 5], Y=[3, 4, 5, 6, 7],
    opts=dict(

        stacked=False,
        layoutopts = dict()
        legend=['Facebook', 'Google', 'Twitter'],
        #rownames=['2012', '2013', '2014', '2015', '2016']

    ))



