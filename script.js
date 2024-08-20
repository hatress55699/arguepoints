// Load the JSON data from db_test.json (ensure the file is accessible)
d3.json('db_test.json').then(function(data) {
    // Set up the SVG canvas dimensions
    const width = window.innerWidth;
    const height = window.innerHeight;

    const svg = d3.select("#graph")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    // Set up the simulation (force-directed layout)
    const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.edges).id(d => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("collision", d3.forceCollide().radius(50));

    // Draw the edges (links)
    const link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(data.edges)
        .enter().append("line")
        .attr("stroke-width", d => Math.sqrt(d.weight))
        .attr("stroke", "#999");

    // Draw the nodes (circles)
    const node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(data.nodes)
        .enter().append("circle")
        .attr("r", 20)
        .attr("fill", d => {
            // Color nodes based on their group
            if (d.group === "Group 1") return "skyblue";
            if (d.group === "Group 2") return "lightgreen";
            if (d.group === "Group 3") return "orange";
            return "gray";
        })
        .call(d3.drag()
            .on("start", dragStarted)
            .on("drag", dragged)
            .on("end", dragEnded));

    // Add labels to the nodes
    const labels = svg.append("g")
        .attr("class", "labels")
        .selectAll("text")
        .data(data.nodes)
        .enter().append("text")
        .attr("dy", 4)
        .attr("dx", -10)
        .attr("font-size", "12px")
        .attr("fill", "#333")
        .text(d => d.label);

    // Update the positions of nodes and edges during simulation
    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        labels
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    });

    // Drag functions for interactivity
    function dragStarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragEnded(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
});
