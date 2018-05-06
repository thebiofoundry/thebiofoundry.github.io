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
	{% assign members = site.members | where: "status", "pi" | sort: "featuredOrder" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<h3>Postdoctoral Researchers</h3>
	<hr><br>
	<div class="row">
	{% assign counter = 0 %}
	{% assign members = site.members | where: "status", "postdoc" | sort: "featuredOrder" %}
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
	{% assign members = site.members | where: "status", "grad" | sort: "featuredOrder" %}
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
	{% assign members = site.members | where: "status", "undergrad" | sort: "featuredOrder" %}
	{% for member in members %}
		{% include member_modal.html member=member counter=counter%}
	{% assign counter=counter | plus:1  %}
	{% endfor %}
	</div>

	<h3>Alumni</h3>
	<hr><br>
	<div class="row">
		<div class="col-md-12 col-sm-12">
		<table class="table table-responsive">
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

