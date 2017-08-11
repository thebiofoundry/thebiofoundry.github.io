---
layout: page
permalink: /members/
title: BioFoundry Members
description: Current members and alumni
---

<!-- <link rel="stylesheet" href="{{ '/assets/css/members.css' | prepend: site.baseurl | prepend: site.url }}"> -->

<br>
<div class="container">
	<!-- <div class="row"> -->
	{% for member in site.members %}
	{% if member.status == 'Current' %}
	<div class="col-md-3 col-sm-6" style="height:161px; outline: none !important;" title="Dismissible popover" data-toggle="popover" data-trigger="focus" tabindex="0"  data-content="{{member.program}}" >
	            <center><img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img"></center>
	            <br>
	            <b> {{ member.title }} </b>
	            <small>{{ member.program }} | since {{ member.year_start }} </small>
	</div>
	{% endif %}
	{% endfor %}
	<!-- </div> -->
</div>


<br>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script>
$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   
});
</script>