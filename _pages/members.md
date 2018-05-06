---
layout: page
permalink: /members/
title: BioFoundry Team
description: Current BioFoundry team members and alumni
---
<div class="container">
	
	<!-- Beginning of PI -->
	<h3>Principal Investigator</h3>
	<hr><br>
	<div class="row">
	{% assign counter = 0 %}
	{% assign members = site.members | where: "status", "pi" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<h3>Postdoctoral Researchers</h3>
	<hr><br>
	<div class="row">
	{% assign counter = 0 %}
	{% assign members = site.members | where: "status", "postdoc" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<!-- Beginning of Grad -->
	<h3>Graduate Students</h3>
	<hr><br>
	<div class="row">
	{% assign counter = 0 %}
	{% assign members = site.members | where: "status", "grad" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<!-- Beginning of Grad -->
	<h3>Undergraduate Students</h3>
	<hr><br>
	<div class="row">
	{% assign counter = 0 %}
	{% assign members = site.members | where: "status", "undergrad" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<h3>Alumni</h3>
	<hr><br>
	<div class="row">
		<div class="col-md-12 col-sm-12 member-block">
		<table class="table">
	    <thead>
	      <tr>
	        <th>Name</th>
	        <th>Current Position</th>
	      </tr>
	    </thead>
	    <tbody>
	    	{% for member in site.members %}
			{% if member.status == 'alumni' %}
		      <tr>
		        <td>{{member.title}}</td>
		        <td>{{member.alumni_position}}</td>
		      </tr>
	    	{% endif %}
			{% endfor %}
		    </tbody>
		  </table>
		</div>
	</div>

</div>

