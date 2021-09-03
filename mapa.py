import pygame
import pytmx


class MapLoader:

    def __init__(self, file):
        tm = pytmx.load_pygame(file, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmdata = tm

    def makeMap(self):
        ti = self.tmdata.get_tile_image_by_gid
        self.layers = []
        for layers in self.tmdata.visible_layers:
            tmpSurface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            if isinstance(layers, pytmx.TiledTileLayer):
                for x, y, gid in layers:
                    tile = ti(gid)
                    if tile:
                        tmpSurface.blit(pygame.transform.scale(tile, (48, 48)), (x * 48, y * 48))
                self.layers.append(tmpSurface)
