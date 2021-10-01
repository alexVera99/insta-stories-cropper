class CropModule:

    def findCropSize(self, width, height, img_width, img_height):
        ratio = width / height
        if(img_width >= img_height):
            self.height = img_height
            self.width = ratio * img_height
        else:
            self.width = img_width
            self.height = img_height/ratio
    
    def limitInBoundaries(self, img_width, img_height):
        if(self.x_min < 0):
            self.x_max += -self.x_min
            self.x_min = 0
        if(self.y_min < 0):
            self.y_max += -self.y_min
            self.y_min = 0
        if(self.x_max > img_width):
            diff = self.x_max - img_width - 1
            self.x_min -= diff
            self.x_max = img_width - 1
        if(self.y_max > img_height):
            diff = self.y_max - img_height - 1
            self.y_min -= diff
            self.y_max = img_height - 1

    def crop(self, img, center):
        img_height, img_width, c = img.shape

        self.x_min = center[0] - int(self.width//2)
        self.y_min = center[1] - int(self.height//2)
        self.x_max = center[0] + int(self.width//2)
        self.y_max = center[1] + int(self.height//2)
        
        self.limitInBoundaries(img_width, img_height)
        #print(self.x_min, self.x_max, self.y_min, self.y_max)
        
        return img[self.y_min:self.y_max, self.x_min:self.x_max, :]