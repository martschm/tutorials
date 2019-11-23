import matplotlib.pyplot as plt
import matplotlib
def neural_net_explanation(i):
    matplotlib.rcParams['text.usetex'] = True
    fig = plt.figure(figsize=(12, 12))
    ax = fig.gca()
    left = 0.1
    right = 0.9
    bottom = 0.1
    top = 0.9
    layer_sizes = [4, 3, 3, 2]
    
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for m in range(layer_size):
            circle = plt.Circle((n*h_spacing + left, layer_top - m*v_spacing), v_spacing/4.,
                                color='w', ec='k', zorder=4)
            ax.add_artist(circle).set_zorder(1)
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k')
                ax.add_artist(line).set_zorder(0)
    ax = fig.gca()
    ax.axis('off')
    
    
    if i >= 1:
        ax.text(0.02, 0.05, r'\textbf{$X_{i}=a^{(0)}_i$}', fontsize=25)
    if i >= 2:
        ax.text(0.08, 0.77, r'\textbf{$a^{(0)}_1$}', fontsize=25).set_zorder(2)
        ax.text(0.08, 0.57, r'\textbf{$a^{(0)}_2$}', fontsize=25).set_zorder(2)
        ax.text(0.08, 0.37, r'\textbf{$a^{(0)}_3$}', fontsize=25).set_zorder(2)
        ax.text(0.08, 0.17, r'\textbf{$a^{(0)}_4$}', fontsize=25).set_zorder(2)
        ax.text(0.08, 0.88, r'\textbf{$a^{(0)}_i$}', fontsize=25).set_zorder(2)
    
    if i >= 3:
        ax.text(0.34, 0.67, r'\textbf{$a^{(1)}_1$}', fontsize=25).set_zorder(2)
        ax.text(0.34, 0.47, r'\textbf{$a^{(1)}_2$}', fontsize=25).set_zorder(2)
        ax.text(0.34, 0.27, r'\textbf{$a^{(1)}_3$}', fontsize=25).set_zorder(2)
        ax.text(0.34, 0.79, r'\textbf{$a^{(1)}_j$}', fontsize=25).set_zorder(2)
    
    if i >= 4:
        ax.text(0.18, 0.82, r'\textbf{$(w^{(1)}_{j,i}, b^{(1)}_j)$}', fontsize=22)
    
    if i >= 5:
        ax.text(0.28, 0.73, r'\textbf{$w^{(1)}_{1,1}$}', fontsize=15)
        ax.text(0.27, 0.68, r'\textbf{$w^{(1)}_{1,2}$}', fontsize=15)
        ax.text(0.28, 0.64, r'\textbf{$w^{(1)}_{1,3}$}', fontsize=15)
        ax.text(0.32, 0.6, r'\textbf{$w^{(1)}_{1,4}$}', fontsize=15)
        ax.text(0.18, 0.71, r'\textbf{$w^{(1)}_{2,1}$}', fontsize=15)
        ax.text(0.11, 0.68, r'\textbf{$w^{(1)}_{3,1}$}', fontsize=15)
    
    if i >= 6:
        ax.text(0.22, 0.17, r'\textbf{$z^{(1)}_j=\sum_i w^{(1)}_{j,i}a^{(0)}_i+b^{(1)}_j$}', fontsize=18)
        ax.text(0.25, 0.05, r'\textbf{$a^{(1)}_j=\frac{1}{1+e^{-z^{(1)}_j}}$}', fontsize=25)
    
    if i >= 7:
        ax.text(0.61, 0.67, r'\textbf{$a^{(2)}_1$}', fontsize=25).set_zorder(2)
        ax.text(0.61, 0.47, r'\textbf{$a^{(2)}_2$}', fontsize=25).set_zorder(2)
        ax.text(0.61, 0.27, r'\textbf{$a^{(2)}_3$}', fontsize=25).set_zorder(2)
        ax.text(0.61, 0.79, r'\textbf{$a^{(2)}_k$}', fontsize=25).set_zorder(2)
    
    if i >= 8:
        ax.text(0.44, 0.73, r'\textbf{$(w^{(2)}_{k,j}, b^{(2)}_k)$}', fontsize=22)
        ax.text(0.55, 0.17, r'\textbf{$z^{(2)}_k=\sum_j w^{(2)}_{k,j}a^{(1)}_j+b^{(2)}_k$}', fontsize=18)
        ax.text(0.55, 0.05, r'\textbf{$a^{(2)}_k=\frac{1}{1+e^{-z^{(2)}_k}}$}', fontsize=25)
    
    if i >= 9:
        ax.text(0.88, 0.57, r'\textbf{$a^{(3)}_1$}', fontsize=25).set_zorder(2)
        ax.text(0.88, 0.37, r'\textbf{$a^{(3)}_2$}', fontsize=25).set_zorder(2)
        ax.text(0.88, 0.7, r'\textbf{$a^{(3)}_l$}', fontsize=25).set_zorder(2)
    
    if i >= 10:
        ax.text(0.72, 0.72, r'\textbf{$(w^{(3)}_{l,k}, b^{(3)}_l)$}', fontsize=22)
        ax.text(0.9, 0.28, r'\textbf{$z^{(3)}_l=\sum_k w^{(3)}_{l,k}a^{(2)}_k+b^{(3)}_l$}', fontsize=18)
        ax.text(0.9, 0.19, r'\textbf{$a^{(3)}_l=\frac{1}{1+e^{-z^{(3)}_l}}$}', fontsize=25)
    
    if i >= 11:
        ax.text(0.95, 0.48, r'\textbf{$E=\frac{1}{2}\sum_l (a_l-y_l)^2$}', fontsize=25)

