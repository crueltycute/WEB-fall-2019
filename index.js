let button = null;

$(onLoad);
function  onLoad() {
    button = $('button');
}

$(() => {
    const from = $('#from');
    const to = $('#to');
    const func = $('#func');
    const plot = $('.plot');

    if (button) {
        button.click((e) => {
            e.preventDefault();

            const fromValue = parseFloat( from.val() );
            const toValue = parseFloat( to.val() );

            const funcValue = ( func.val() );

            const points = [];
            for (let x = fromValue; x <= toValue; x += 0.01 )
                points.push([x, eval(funcValue)]);

            $.plot(plot, [{ label: funcValue, data: points }], [points], {});
        });
    }
});
