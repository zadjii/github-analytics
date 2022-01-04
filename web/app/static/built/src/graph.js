class GraphPage {
    constructor() {
        this.my_graph = null;
        this.my_categories_graph = null;
        this.error_row = null;
        this.start_date_input = null;
        this.end_date_input = null;
        this.category_input = null;
        this.my_graph = $("#my-graph");
        this.my_categories_graph = $("#my-categories-graph");
        this.error_row = $("#error-row");
        this.start_date_input = $("#start-date");
        this.end_date_input = $("#end-date");
        this.category_input = $("#category-input");
        this.start_date_input.change(() => { this.update(); });
        this.end_date_input.change(() => { this.update(); });
        this.category_input.change(() => { this.update(); });
    }
    update() {
        this.clear_state();
    }
    clear_state() {
        this.clear_error();
        this.my_graph.empty();
        this.my_categories_graph.empty();
    }
    clear_error() {
        this.error_row.css("display", "none");
    }
}
;
$(document).ready(function () {
    log_div = $("#my-log");
    let state = new GraphPage();
    state.update();
});
