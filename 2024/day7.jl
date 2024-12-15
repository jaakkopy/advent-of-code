id1 = (a,b) -> a
f1 = (a,b) -> a + b
f2 = (a,b) -> a - b
f3 = (a,b) -> a * b
f4 = (a,b) -> parse(Int64, string(a)*string(b))


function evaluate1(i, nums, x, f, target)
    x = f(x, nums[i])
    if i == length(nums)
        return x == target
    end
    plus = evaluate1(i+1, nums, x, f1, target)
    minus = evaluate1(i+1, nums, x, f2, target)
    mul = evaluate1(i+1, nums, x, f3, target)
    return (plus || minus || mul)
end


function evaluate2(i, nums, x, f, target)
    x = f(x, nums[i])
    if i == length(nums)
        return x == target
    end
    plus = evaluate2(i+1, nums, x, f1, target)
    minus = evaluate2(i+1, nums, x, f2, target)
    mul = evaluate2(i+1, nums, x, f3, target)
    cat = evaluate2(i+1, nums, x, f4, target)
    return (plus || minus || mul || cat)
end


function main()
    s1 = 0
    s2 = 0

    while !eof(stdin)
        line = readline(stdin)
        if isempty(line)
            break
        end
        (target, nums) = split(line, ':')
        nums = parse.(Int64, split(nums))
        target = parse(Int64, target)

        if evaluate1(1, nums, nums[1], id1, target)
            s1 += target
        end
        if evaluate2(1, nums, nums[1], id1, target)
            s2 += target
        end

    end

    println(s1)
    println(s2)

end

main()