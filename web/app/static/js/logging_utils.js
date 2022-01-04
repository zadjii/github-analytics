
////////////////////////////////////////////////////////////////////////////////
// Logging
////////////////////////////////////////////////////////////////////////////////
var log_div;

function mylog(text) {
    console.log(text);
    pagelog(text);
}

function pagelog(text) {
    log_div.append($("<div>").text(text));
}

function pagelog_element(elem, header){
    log_div.append($("<p>"));
    if (header) log_div.append($("<h3>").text(header));
    log_div.append(elem);
}

function syntaxHighlight(json) {
    if (typeof json != 'string') {
         json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}
function pagelog_as_json(obj) {
    var text = JSON.stringify(obj, null, 2);
    text = syntaxHighlight(text);
    log_div.append(
        $("<pre>")
            .html(text)
    );
}

var formatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
  minimumFractionDigits: 2,
});

function format_money(value){
    return formatter.format(value);
}
////////////////////////////////////////////////////////////////////////////////

function easy_table(objs) {
    var obj_0 = objs[0];

    var table_root = $("<div>");
    var table = $("<table>");
    var thead = $("<thead>");
    var tbody = $("<tbody>");
    var thead_row = $("<tr>");

    Object.keys(obj_0).map(function(key, index) {
        var cell = $("<td>");
        // console.log(key);
        cell.text(key);
        cell
            .css("border-style", "solid")
            .css("border-width", "1px")
            .css("padding-left", "4px")
            .css("margin", "0px")
        ;
        if (index > 0) cell.css("text-align", "right")

        thead_row.append(cell);
    });

    // border-style: solid;
    // border-width: 1px;
    // padding: 4px;

    objs.map(function(obj) {
        var tbody_row = $("<tr>");
        Object.keys(obj).map(function(key, index) {
            var cell = $("<td>");
            cell.text(obj[key]);
            tbody_row.append(cell);
            cell
                .css("border-style", "solid")
                .css("border-width", "1px")
                .css("padding", "4px")
            .css("margin", "0px")
            ;
            if (index > 0) cell.css("text-align", "right")
        });
        tbody.append(tbody_row)
    });

    thead.append(thead_row);
    table.append(thead);
    table.append(tbody);
    table_root.append(table);

    return table_root;
}
