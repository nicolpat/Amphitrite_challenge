import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import cmocean
from matplotlib import colors

# create colormap

def create_figure(box_frame=None):
    if box_frame is None:
        box_frame = [-180, 180, -90, 90]

    plt.rcParams["figure.figsize"] = [10.00, 5]

    plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    gls = ax.gridlines(draw_labels=True)
    gls.top_labels = False  # suppress top labels
    gls.right_labels = False  # suppress right labels
    plt.axis(box_frame)


def add_variability_absolute_dynamical_topography(array, marker = 'o',color='black'):
    # Create color map of fixed colors
    cmap = colors.ListedColormap(['lightgray','orange', 'red'])
    bounds = [0, .1, .2, .3]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.scatter(array.longitude, array.latitude,
                      c = array.std_adt,
                      s = 100,
                      cmap=cmap, norm=norm,
                      marker=marker,
                      edgecolor = color)
    plt.clim(0,.3)
def add_absolute_dynamical_topography(array, marker = 'o',color='black'):
    # Create color map of fixed colors
    plt.scatter(array.longitude, array.latitude,
                c=array.adt,
                s = 100,
                cmap=cmocean.cm.balance,
                marker=marker,
                edgecolor=color)
    plt.clim(-1.5,1.5)


def add_track(array, color='black'):
    plt.scatter(array.longitude, array.latitude, c=color, s=1, marker=".")


def display_figure(title='',legend='',colorbar_unit = '',display = False,savefig=False):
    plt.title(title)
    plt.colorbar(label=colorbar_unit, shrink=0.5)
    plt.legend(legend)
    if savefig is True:
        plt.savefig(f'figure/{title}.png',dpi=300)
    if display is True:
        plt.show()
