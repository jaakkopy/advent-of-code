function dependency_sort(update, edges)
    L = []
    pred = Dict()

    for u in update
        pred[u] = []
        for (a,b) in edges
            if b == u && a in update
                push!(pred[u], a)
            end
        end
    end 

    while length(update) > 0
        # Find the vertex which has no predecessor dependencies
        # from the set of remaining vertices and add it to L
        l = length(update)
        for i in 1:l
            u = update[i]
            no_pred = true
            for j in 1:l
                w = update[j]
                if i == j
                    continue
                end
                if w in pred[u]
                    no_pred = false
                    break
                end
            end
            if no_pred
                push!(L, u)
                popat!(update, i)
                break
            end
        end
    end

    return L
end


function main()
    # Edges in the dependency grap. (a,b) means b depends on a
    edges = Set()
    
    while !eof(stdin)
        line = readline(stdin)
        if isempty(line)
            break
        end
        (a,b) = parse.(Int32, split(line, '|'))
        push!(edges, (a,b))
    end

    part1 = 0 
    part2 = 0

    while !eof(stdin)
        line = readline(stdin)
        update = parse.(Int32, collect(split(line, ',')))
        
        ok = true
        l = length(update)

        for i in 1:l
            x = update[i]
            # Is a predecessor dependency found after?
            for j in (i+1):l
                y = update[j]
                if (y,x) in edges
                    ok = false
                    break
                end
            end
        end

        if ok
            if l > 0
                part1 += update[div(l,2)+1]
            end
        else
            if l > 0
                sorted = dependency_sort(update, edges)
                part2 += sorted[div(l,2)+1]
            end
        end

    end

    println(part1)
    println(part2)
end


main()