function []= plot_things(plot_matrix)

    % Errore
    x = [1, 2, 3, 4, 5, 6, 7, 8];
    y1 = plot_matrix(:,3)';
    disp(y1)
    p = semilogy(x, y1,'b--o','MarkerSize', 5);
    p.Color = 'r';
    xticks([1 2 3 4 5 6 7 8])
    xticklabels({'GT01R','TSCOPF','ns3Da','nd24k', 'ifiss', 'bundleadj', 'Hook1498', 'G3circuit'})
    xlabel ('Matrix Dimension')
    legend('Error')
    title('Error')
    grid on
    
    % Tempo
    figure
    x = [1, 2, 3, 4, 5, 6, 7, 8];
    y2 = [plot_matrix(:,4)]';
    disp(y2)
    q = semilogy(x, y2,'b--o','MarkerSize', 5);
    q.Color = 'g';
    xticks([1 2 3 4 5 6 7 8])
    xticklabels({'GT01R','TSCOPF','ns3Da','nd24k', 'ifiss', 'bundleadj', 'Hook1498', 'G3circuit'})
    xlabel ('Matrix Dimension')
    legend('Time')
    title('Time')
    grid on

    %Memory
    figure
    x = [1, 2, 3, 4, 5, 6, 7, 8];
    y3 = [plot_matrix(:,5)]';
    disp(y3)
    s = semilogy(x, y3,'b--o','MarkerSize', 5);
    s.Color = 'b';
    xticks([1 2 3 4 5 6 7 8])
    xticklabels({'GT01R','TSCOPF','ns3Da','nd24k', 'ifiss', 'bundleadj', 'Hook1498', 'G3circuit'})
    xlabel ('Matrix Dimension')
    legend('Memory')
    title('Memory')
    grid on
end



