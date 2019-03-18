import visdom
import matplotlib.pyplot as plt
import io


entrada = [{
       "x_Axis": 72,
       "y_Axis": 219,
       "width": 24,
       "Height": 41,
       "color": "yellow"
   },
   {
       "x_Axis": 127,
       "y_Axis": 134,
       "width": 19,
       "Height": 51,
       "color": "red"
   },
   {
       "x_Axis": 94,
       "y_Axis": 145,
       "width": 22,
       "Height": 43,
       "color": "red"
   },
   {
       "x_Axis": 157,
       "y_Axis": 117,
       "width": 20,
       "Height": 59,
       "color": "orange"
   },
   {
       "x_Axis": 106,
       "y_Axis": 217,
       "width": 25,
       "Height": 43,
       "color": "blue"
   },
   {
       "x_Axis": 178,
       "y_Axis": 225,
       "width": 22,
       "Height": 31,
       "color": "green"
   },
   {
       "x_Axis": 144,
       "y_Axis": 226,
       "width": 20,
       "Height": 29,
       "color": "green"
   }]

print(entrada[1]["Height"])
print(len(entrada))

def gerar_barras(entrada):
    quantidade = len(entrada)
    position_x = []
    valorbar = []
    fig, ax = plt.subplots()
    #plt.bar([1,2,3,4], entrada[0]["Height"], 0.8)
    for i in range(0, quantidade):
        position_x.append(i)
        valorbar.append(entrada[i]["Height"])

    #barlist = plt.bar([1, 2, 3, 4], [1, 2, 3, 4])
    #barlist[0].set_color('r')

    barlist = plt.bar(position_x, valorbar)
    for i in range(0, quantidade):
        barlist[i].set_color(entrada[i]["color"])

    vis = visdom.Visdom()
    vis.close(win=None)
    return vis.matplot(plt)

    #return vis.bar()
    #return plt.show()



gerar_barras(entrada)