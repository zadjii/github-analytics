

class GraphPage {

    my_graph : JQuery<HTMLElement> = null;
    my_categories_graph : JQuery<HTMLElement> = null;
    error_row : JQuery<HTMLElement> = null;
    start_date_input : JQuery<HTMLElement> = null;
    end_date_input : JQuery<HTMLElement> = null;
    category_input : JQuery<HTMLElement> = null;

    constructor() {
        this.my_graph = $("#my-graph");
        this.my_categories_graph = $("#my-categories-graph");
        this.error_row = $("#error-row");
        this.start_date_input = $("#start-date");
        this.end_date_input = $("#end-date");
        this.category_input = $("#category-input");

        this.start_date_input.change(()=>{ this.update(); });
        this.end_date_input.change(()=>{ this.update(); });
        this.category_input.change(()=>{ this.update(); });
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

};

$(document).ready(function(){
    log_div = $("#my-log");

    let state : GraphPage = new GraphPage();
    state.update();
});


