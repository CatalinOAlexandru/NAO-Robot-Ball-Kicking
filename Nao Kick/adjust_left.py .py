#-*- coding: iso-8859-15 -*-

'''Walk To: Small example to make Nao Walk To an Objective '''
'''         With customization '''

import config

def main():
    motionProxy = config.loadProxy("ALMotion")

    # Set NAO in stiffness On
    config.StiffnessOn(motionProxy)

    x     = 0.0
    y     = 0.05
    theta = 0.0

   # parameters are set to the default value
    motionProxy.walkTo(x, y, theta, [ ["StepHeight", 0.02] ]) # step height of 4 cm

if __name__ == "__main__":
    main()
