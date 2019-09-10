command: "cd stock-tracker.widget/ && python gatherData.py"

refreshFrequency: 60000

style: """
    top: 180px
    left: 270px
    margin-left: -260px
    font-family: Helvetica Neue

    table, th, td
        text-align: center
        border: 1px solid black
        border-collapse: collapse
        color: white
        padding: 3px
        font-size: 15px
        font-weight: lighter
        font-smoothing: antialiased
        background: #334B7C
"""

render: -> """
    <table>
        <tbody></tbody>
    </table>
"""

getPrice: (output, table) ->

    tbody = table.find("tbody")
    tbody.empty()
    tbody.append "<tr><td>Ticker</td><td>Price</td><td>Change</td><td>%</td></tr>"
    tbody.append output

update: (output, domEl) ->
    table = $(domEl).find("table")

    @getPrice output, table
