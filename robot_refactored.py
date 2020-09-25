from abc import ABC, abstractmethod 

class Robot:

  def __init__(self, bipedal="", quadripedal= "", wheeled="", flying="", traversal=[], detection_systems=[]):
    self.bipedal = bipedal
    self.quadripedal = quadripedal
    self.wheeled = wheeled
    self.flying = flying
    self.traversal = traversal
    self.detection_systems = detection_systems

  def __str__(self):

    string = f"{self.bipedal}{self.quadripedal}{self.wheeled}{self.flying} ROBOT. \n"
    if self.traversal:
      string += "Traversal modules installed:\n"
    for module in self.traversal:
      string += "- " + str(module) + "\n"
    if self.detection_systems:
      string += "Detection systems installed:\n"
    for system in self.detection_systems:
      string += "- " + str(system) + "\n"

    return string

class BipedalLegs:
  def __str__(self):
    return "two legs"

class QuadripedalLegs:
  def __str__(self):
    return "four legs"

class Arms:
  def __str__(self):
    return "two arms"

class Wings:
  def __str__(self):
    return "wings"

class Blades:
  def __str__(self):
    return "blades"

class FourWheels:
  def __str__(self):
    return "four wheels"

class TwoWheels:
  def __str__(self):
    return "two wheels"

class CameraDetectionSystem:
  def __str__(self):
    return "cameras"

class InfraredDetectionSystem:
  def __str__(self):
    return "infrared"


class RobotBuilder(ABC):
    
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  @abstractmethod
  def build_traversal(self):
    pass

  @abstractmethod
  def build_detection_system(self):
    pass

  @abstractmethod
  def set_type(self):
    pass

  def get_product(self):
    return self.product
    
# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
  
  def set_type(self):
    self.product.bipedal = "BIPEDAL"

  def build_traversal(self):
    self.product.traversal.clear()
    self.product.detection_systems.clear()
    self.product.traversal.append(BipedalLegs())
    self.product.traversal.append(Arms())
    
  def build_detection_system(self):
    self.product.detection_systems.append(CameraDetectionSystem())
    
# Concrete Builder class:  there would be many of these
class AutonomousCarBuilder(RobotBuilder):

  def set_type(self):
    self.product.wheeled = "WHEELED"

  def build_traversal(self):
    self.product.traversal.clear()
    self.product.detection_systems.clear()
    self.product.traversal.append(FourWheels())
    
  def build_detection_system(self):
    self.product.detection_systems.append(InfraredDetectionSystem())
    

#new type of Robot
class FlyingBattleBot(RobotBuilder):

  def set_type(self):
    self.product.flying = "FLYING"

  def build_traversal(self):
    self.product.traversal.clear()
    self.product.detection_systems.clear()
    self.product.traversal.append(TwoWheels())
    self.product.traversal.append(Wings())
    self.product.traversal.append(Blades())
    

  def build_detection_system(self):
    self.product.detection_systems.append(InfraredDetectionSystem())
    self.product.detection_systems.append(CameraDetectionSystem())
  

class Director:
    def make_robot(self, builder):
        builder.set_type()
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

def main():
  director = Director()

  builder = AndroidBuilder()
  print(director.make_robot(builder))

  builder = AutonomousCarBuilder()
  print(director.make_robot(builder))

  builder = FlyingBattleBot()
  print(director.make_robot(builder))

if __name__ == "__main__":
  main()
