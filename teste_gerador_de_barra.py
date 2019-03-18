import visdom_barra as bar

entrada = [
   {
       "Height": 41,
       "color": "yellow",
       "center": 83
   },
   {
       "Height": 43,
       "color": "red",
       "center": 105
   },
   {
       "Height": 42,
       "color": "blue",
       "center": 118
   },
   {
       "Height": 51,
       "color": "red",
       "center": 135
   },
   {
       "Height": 29,
       "color": "green",
       "center": 153
   },
   {
       "Height": 59,
       "color": "orange",
       "center": 166
   },
   {
       "Height": 31,
       "color": "green",
       "center": 188
   }
]

bar.gerar_barras(entrada)
