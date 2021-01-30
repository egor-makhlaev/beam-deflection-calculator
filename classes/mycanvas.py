from tkinter import Canvas, PhotoImage


class MyCanvas(Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self._images = {}
        self._image_on_canvas = None

    def set_image(self, image_path):
        images = self._images
        img_on_cnvs = self._image_on_canvas

        if image_path in images:
            image = images[image_path]
        else:
            image = PhotoImage(file=image_path)
            images.update({image_path: image})

        if img_on_cnvs is None:
            self._image_on_canvas = self.create_image(
                0,
                0,
                image=image,
                anchor="nw"
            )
        else:
            self.itemconfig(
                img_on_cnvs,
                image=image
            )

    def reset(self):
        self._image_on_canvas = None
        self.delete("all")
