from Objects.Game3DObjects import *

class OneHitBrick(Brick):
    def __init__(self, position, width, height, color, textures):
        super().__init__(position, width, height, color)
        self.hitCount = 1
        self.currentHits = 0
        self.textures = textures

    def update(self):
        if self.collided:
            self.collided = False
            if self.currentHits == 3:
                pass
            else:
                self.currentHits += 1

    def display(self, model_matrix, shader):
        # if self.currentHits != 0:
        #     shader.set_using_tex(1.0)
        #     glActiveTexture(GL_TEXTURE0)
        #     glBindTexture(GL_TEXTURE_2D, self.textures[self.currentHits - 1])
        #     shader.set_dif_tex(0)
        #     shader.set_using_tex(0.0)

        super().display(model_matrix, shader)