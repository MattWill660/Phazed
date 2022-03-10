import os
import sys
from phazedapp.phazed import PhazedApp

basepath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, basepath)

def main():
    PhazedApp().run()


if __name__ == '__main__':
    main()
