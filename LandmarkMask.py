# A bunch of useful functions in order to extract a mask for each Landmark 



def vertices_circles(index_shapeData, shapeData):
    import numpy as np 
    """Returns vertices coordinates for Circle Small and Circle Large masks """
    
    radius_small_circle = 0.038 # 7.6 cm (check Jun et al. paper)
    radius_large_circle = 0.051 # 10.2 cm (check Jun et al. paper)

    # We should decide whether this is a good candidate as a value
    radius_small_mask = radius_small_circle + 0.03 # 3cm is related to fish senses (check Jun et al paper)
    radius_large_mask =  radius_large_circle + 0.03 



    x_pos_vertex = []
    y_pos_vertex = [] 
    number_of_vertices = 1000 # 1000 Are enough to get a good approximate result 


    for m in range(0, number_of_vertices): 
        x_pos_vertex.append(np.cos(2*m *np.pi/number_of_vertices  ))
        y_pos_vertex.append(np.sin(2*m *np.pi/number_of_vertices  ))

    x_pos_vertex = np.asarray(x_pos_vertex)
    y_pos_vertex = np.asarray(y_pos_vertex)

    x0_small_circle = shapeData[index_shapeData].iloc[5,1]
    y0_small_circle = shapeData[index_shapeData].iloc[5,2]
    x0_large_circle = shapeData[index_shapeData].iloc[4,1]
    y0_large_circle = shapeData[index_shapeData].iloc[4,2]

    x_pos_vertex_small_circle_mask = radius_small_mask*x_pos_vertex + x0_small_circle
    y_pos_vertex_small_circle_mask = radius_small_mask*y_pos_vertex + y0_small_circle
    x_pos_vertex_large_circle_mask = radius_large_mask*x_pos_vertex + x0_large_circle
    y_pos_vertex_large_circle_mask = radius_large_mask*y_pos_vertex + y0_large_circle


    vertex_coordinates_large_circle_mask = np.vstack((x_pos_vertex_large_circle_mask, y_pos_vertex_large_circle_mask)).T
    vertex_coordinates_small_circle_mask = np.vstack((x_pos_vertex_small_circle_mask, y_pos_vertex_small_circle_mask)).T
    
    return vertex_coordinates_small_circle_mask, vertex_coordinates_large_circle_mask


def vertices_squares(index_shapeData, shapeData):
    import numpy as np 
    """Returns vertices coordinates for Square Small and Square Large masks """
    side_small_square = 0.056 # 5.6 cm (check Jun et al. paper)
    side_large_square = 0.09 # 9.0 cm (check Jun et al. paper)

    # We should decide whether this is a good candidate as a value
    side_small_mask = side_small_square + 0.03 # 3cm is related to fish senses (check Jun et al paper)
    side_large_mask = side_large_square + 0.03 



    x_pos_vertex_square = []
    y_pos_vertex_square = [] 
    number_of_vertices_square = 4 

    # Adding pi/4 rotation because our squares vertices don't start from angle = 0 
    for m in range(0, number_of_vertices_square) : 
        x_pos_vertex_square.append(np.cos(2*m *np.pi/number_of_vertices_square  +np.pi/4))
        y_pos_vertex_square.append(np.sin(2*m *np.pi/number_of_vertices_square  +np.pi/4))

    x_pos_vertex_square = np.asarray(x_pos_vertex_square)
    y_pos_vertex_square = np.asarray(y_pos_vertex_square)

    x0_small_square = shapeData[index_shapeData].iloc[3,1]
    y0_small_square = shapeData[index_shapeData].iloc[3,2]
    x0_large_square = shapeData[index_shapeData].iloc[2,1]
    y0_large_square = shapeData[index_shapeData].iloc[2,2]

    diagonal_small_square_mask = np.sqrt(2)*side_small_mask  
    diagonal_large_square_mask = np.sqrt(2)*side_large_mask

    x_pos_vertex_small_square_mask = (diagonal_small_square_mask/2)*x_pos_vertex_square + x0_small_square
    y_pos_vertex_small_square_mask = (diagonal_small_square_mask/2)*y_pos_vertex_square + y0_small_square
    x_pos_vertex_large_square_mask = (diagonal_large_square_mask/2)*x_pos_vertex_square + x0_large_square
    y_pos_vertex_large_square_mask = (diagonal_large_square_mask/2)*y_pos_vertex_square + y0_large_square


    vertex_coordinates_small_square_mask = np.vstack((x_pos_vertex_small_square_mask, y_pos_vertex_small_square_mask)).T
    vertex_coordinates_large_square_mask = np.vstack((x_pos_vertex_large_square_mask, y_pos_vertex_large_square_mask)).T
    
    return vertex_coordinates_small_square_mask, vertex_coordinates_large_square_mask

def vertices_triangles(index_shapeData, shapeData):
    import numpy as np 
    """Returns vertices coordinates of Triangle Small and Triangle Large masks"""
    
    side_small_triangle = 0.072 # 7.2 cm (check Jun et al. paper)
    side_large_triangle = 0.132 # 13.2 cm (check Jun et al. paper)

    # We should decide whether this is a good candidate as a value
    side_small_mask_triangle = side_small_triangle + (2/np.sqrt(3))*0.03 # 3cm is related to fish senses (check Jun et al paper)
    side_large_mask_triangle = side_large_triangle + (2/np.sqrt(3))*0.03 



    x_pos_vertex_triangle_small = []
    y_pos_vertex_triangle_small = []

    x_pos_vertex_triangle_large = []
    y_pos_vertex_triangle_large = []

    number_of_vertices_triangle = 3 

    # Adding pi/4 rotation because our triangles vertices don't start from angle = 0 
    for m in range(0, number_of_vertices_triangle) : 
        x_pos_vertex_triangle_small.append(np.cos(2*m *np.pi/number_of_vertices_triangle  + np.pi/2 - np.radians(shapeData[index_shapeData].iloc[1,3])))
        y_pos_vertex_triangle_small.append(np.sin(2*m *np.pi/number_of_vertices_triangle  + np.pi/2 - np.radians(shapeData[index_shapeData].iloc[1,3])))
    
        x_pos_vertex_triangle_large.append(np.cos(2*m *np.pi/number_of_vertices_triangle  + np.pi/2 - np.radians(shapeData[index_shapeData].iloc[0,3])))
        y_pos_vertex_triangle_large.append(np.sin(2*m *np.pi/number_of_vertices_triangle  + np.pi/2 - np.radians(shapeData[index_shapeData].iloc[0,3])))

    x_pos_vertex_triangle_small = np.asarray(x_pos_vertex_triangle_small)
    y_pos_vertex_triangle_small = np.asarray(y_pos_vertex_triangle_small)

    x_pos_vertex_triangle_large = np.asarray(x_pos_vertex_triangle_large)
    y_pos_vertex_triangle_large = np.asarray(y_pos_vertex_triangle_large)


    x0_small_triangle = shapeData[index_shapeData].iloc[1,1]
    y0_small_triangle = shapeData[index_shapeData].iloc[1,2]
    x0_large_triangle = shapeData[index_shapeData].iloc[0,1]
    y0_large_triangle = shapeData[index_shapeData].iloc[0,2]

    radius_from_small_triangle_side = side_small_mask_triangle/np.sqrt(3)
    radius_from_large_triangle_side = side_large_mask_triangle/np.sqrt(3)

    x_pos_vertex_small_triangle_mask = radius_from_small_triangle_side*x_pos_vertex_triangle_small + x0_small_triangle
    y_pos_vertex_small_triangle_mask = radius_from_small_triangle_side*y_pos_vertex_triangle_small + y0_small_triangle
    x_pos_vertex_large_triangle_mask = radius_from_large_triangle_side*x_pos_vertex_triangle_large + x0_large_triangle
    y_pos_vertex_large_triangle_mask = radius_from_large_triangle_side*y_pos_vertex_triangle_large + y0_large_triangle


    vertex_coordinates_small_triangle_mask = np.vstack((x_pos_vertex_small_triangle_mask, y_pos_vertex_small_triangle_mask)).T
    vertex_coordinates_large_triangle_mask = np.vstack((x_pos_vertex_large_triangle_mask, y_pos_vertex_large_triangle_mask)).T
    
    return vertex_coordinates_small_triangle_mask, vertex_coordinates_large_triangle_mask

def circle_around_food(index_shapeData,shapeData):
    import numpy as np 
    """Returns food mask coordinates"""
    radius_food = 0.0
     
    radius_food_mask = radius_food + 0.04 # 4 cm check on Jun et Al. paper

    x_pos_vertex = []
    y_pos_vertex = [] 
    number_of_vertices = 1000 # 1000 Are enough to get a good approximate result 


    for m in range(0, number_of_vertices) : 
        x_pos_vertex.append(np.cos(2*m *np.pi/number_of_vertices  ))
        y_pos_vertex.append(np.sin(2*m *np.pi/number_of_vertices  ))

    x_pos_vertex = np.asarray(x_pos_vertex)
    y_pos_vertex = np.asarray(y_pos_vertex)

    x0_food = shapeData[index_shapeData].iloc[6,1]
    y0_food = shapeData[index_shapeData].iloc[6,2]

    x_pos_vertex_food_mask = radius_food_mask*x_pos_vertex + x0_food
    y_pos_vertex_food_mask = radius_food_mask*y_pos_vertex + y0_food

    vertex_coordinates_food_mask = np.vstack((x_pos_vertex_food_mask, y_pos_vertex_food_mask)).T
    
    return vertex_coordinates_food_mask
