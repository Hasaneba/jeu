import pygame

# definir une classe qui va s'occuper les animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la creation de l'entite
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'PygameAssets-main/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self,  loop=False):

        # verifier si l'animation est active
        if self.animation:

            # passer a l'image suivante
            self.current_image += 1

            # verifier si on a  atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remetre l'animation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:

                    # desactivation l'animation
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # reuperer le chemin du dossier pour ce sprite
    path = f'PygameAssets-main/{sprite_name}/{sprite_name}'

    # boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str (num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui vq contenir les images chargees de chaque sprite
# mummy -> [....mummy1.png, ...mummy2.png, ...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}