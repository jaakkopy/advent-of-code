function inbounds(p, a, b)
    (i,j) = p
    return !(i < 1 || i > a || j < 1 || j > b)
end


function check1(p, lines, dir, start)
    if start == 'X'
        xmas = "XMAS"
    else
        xmas = "SAMX"
    end
    a = length(lines)
    b = length(lines[1])
    for k in 1:4
        (i,j) = p
        if !inbounds(p, a, b)
            return 0
        end
        if lines[i][j] != xmas[k]
            return 0
        end
        p += dir 
    end
    return 1
end


function check2(p, lines)
    a = length(lines)
    b = length(lines[1])

    p1 = p + [-1,-1];
    p2 = p + [-1,1];
    p3 = p + [1,-1];
    p4 = p + [1,1];

    for x in [p1, p2, p3, p4]
        if !inbounds(x, a, b)
            return 0
        end
    end

    x1 = lines[p1[1]][p1[2]]
    x2 = lines[p2[1]][p2[2]]
    x3 = lines[p3[1]][p3[2]]
    x4 = lines[p4[1]][p4[2]]

    valid = [['M', 'M', 'S', 'S'], ['S', 'S', 'M', 'M'], ['S', 'M', 'S', 'M'], ['M', 'S', 'M', 'S']]

    for v in valid
        if [x1, x2, x3, x4] == v
            return 1
        end
    end

    return 0
end


function main()
    lines = Vector{String}()
    while !eof(stdin)
        line = readline(stdin)
        push!(lines, line)
    end
    n = length(lines)
    m = length(lines[1])
    xmas = 0
    x_mas = 0
    for i in 1:n
        for j in 1:m
            if lines[i][j] == 'X' || lines[i][j] == 'S'
                # Only check above (left, right, up, diagonals) to not check the same string twice
                for dir in [[-1,0], [-1,-1], [1,-1], [0,1]]
                    xmas += check1([i,j], lines, dir, lines[i][j])
                end
            end
            if lines[i][j] == 'A'
                x_mas += check2([i,j], lines)
            end
        end
    end
    println(xmas)
    println(x_mas)
end

main()