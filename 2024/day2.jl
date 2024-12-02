function check_report(v, condition, allow_fix)
    l = length(v)
    i = 2
    while i <= l
        if ~condition(v[i], v[i-1])
            if ~allow_fix
                return 0
            end
            # remove both of the possible faulty elements and check again
            # set allow_fix = false, since only one fix is allowed
            return min(1, check_report([v[1:(i-1)];v[(i+1):l]], condition, false) + check_report([v[1:(i-2)];v[i:l]], condition, false))
        end
        i = i + 1;
    end
    return 1
end


function main()
    reports = Vector{Int32}[]
    while !eof(stdin)
        line = readline(stdin)
        nums = parse.(Int32, collect(eachsplit(line)))
        push!(reports, nums)
    end
    safe1 = 0
    safe2 = 0
    incr(a,b) = (1 <= a - b <= 3)
    decr(a,b) = (1 <= b - a <= 3)
    for v in reports
        safe1 += min(1, check_report(v, incr, false) + check_report(v, decr, false))
        safe2 += min(1, check_report(v, incr, true) + check_report(v, decr, true))
    end
    println(safe1)
    println(safe2)

end

main()
