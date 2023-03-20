function match(problem_url, problem) {
    problem_url = problem_url.toLowerCase();
    const problem_url_parts = problem_url.split("/");
    if (problem["index"] && !problem_url_parts.includes(problem["index"].toLowerCase()))
        return false;
    if (problem["contestId"] && !problem_url_parts.includes(String(problem["contestId"]).toLowerCase()))
        return false;
    
    return true;
}

function get_problems_table() {
    var tables = document.getElementsByTagName("table");
    return tables[tables.length - 1];
}

function update_problemset_table(user_status) {
    problems_table = get_problems_table();
    for (var row of problems_table.rows) {
        let problem_cell = row.cells[0];
        a_tags = problem_cell.getElementsByTagName("a");
        if (a_tags.length == 0) continue;

        const problem_url = a_tags[0].href;
        if (!problem_url) continue;

        var problem_status = 0;
        for (const submission of user_status) {
            if (match(problem_url, submission["problem"])) {
                problem_status = Math.max(problem_status, 1);
                if (submission["verdict"] == "OK")
                    problem_status = Math.max(problem_status, 2);
            }
        }

        if (problem_status == 2)
            row.classList.add("solved-row");
    }
}

function clear() {
    problems_table = get_problems_table();
    for (var row of problems_table.rows) {
        row.classList.remove("solved-row");
    }
}

function cf_status_checker() {
    clear();
    
    const cf_handel = document.forms["cf-handel-form"]["cf-handel"].value;
    const api_url = "https://codeforces.com/api/user.status?handle=" + cf_handel;

    fetch(api_url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        }
    }).then(response => response.json()).then(response => {
        if (response.status == "OK")
            update_problemset_table(response.result);
    });

    return false;
}