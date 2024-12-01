function main()
    A1 = Vector{Int32}()
    A2 = Vector{Int32}()
    while !eof(stdin)
        line = readline(stdin)
        nums = parse.(Int32, collect(eachsplit(line)))
        push!(A1, nums[1])
        push!(A2, nums[2])
    end
    A1 = sort(A1)
    A2 = sort(A2)
    # part 1
    println(sum(abs.(A1 - A2)))

    # part 2
    counts = map(x -> count(==(x), A2), A1)
    println(sum(A1 .* counts))
end

main()
