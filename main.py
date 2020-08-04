
import sys
from processing import refine, generate_graph


if __name__ == '__main__':
    
    print("(1/2): Processing data")
    refined_data = refine(sys.argv[1])
    
    print("(2/2): Generating graph")
    try: 
        generate_graph(refined_data, int(sys.argv[2]))
    except IndexError:
        generate_graph(refined_data, 20)
