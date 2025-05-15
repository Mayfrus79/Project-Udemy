class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming
    
    def start_filming(self):
        if self.filming:
            print(f'{self.name} is already filming...')
            return
        print(f'{self.name} is now filming...')
        self.filming = True
        
    def stop_filming(self):
        print(f'{self.name} is stopping filming...')
        self.filming = False
        if not self.filming:
            print(f'{self.name} is not filming...')
            return
    
    def take_picture(self):
        print(f'{self.name} is taking a picture...')
        if self.filming:
            print(f'{self.name} cannot take pictures while filming!')
            return  


c1 = Camera('Canon')  # Create Canon camera object
c2 = Camera('Sony')  # Create Sony camera object
# Canon actions
c1.start_filming()  # Start filming with Canon
c1.start_filming()  # Attempt to start filming again (already filming)
c1.take_picture()  # Try taking a picture while filming
c1.stop_filming()  # Stop filming with Canon
c1.take_picture()  # Take a picture after stopping filming
print()
# Sony actions
c2.stop_filming()  # Try stopping filming (not filming yet)
c2.start_filming()  # Start filming with Sony
c2.start_filming()  # Attempt to start filming again (already filming)
c2.take_picture()  # Try taking a picture while filming
c2.stop_filming()  # Stop filming with Sony
c2.take_picture()  # Take a picture after stopping filming
