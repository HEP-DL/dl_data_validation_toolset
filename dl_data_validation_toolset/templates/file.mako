<%inherit file="base.mako"/>

<%block name="body_content">

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h1>File Report For: ${file_report.filename}</h1>
    </div>
  <div class='col-md-1'></div>
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
  <h2>Passing: 
%if file_report.valid :
      <span class="label label-success"> Valid</span>
%else:
      <span class="label label-danger"> Invalid</span>
%endif
  </h2>
    </div>
  <div class='col-md-1'></div>    
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
  <h2>Test Results</h2>
  <table class="table table-hover">
    <tr>
    <th>Name</th><th>Passed</th><th>Fields</th>
    </tr>
  % for result in file_report.reports:
      <tr
        %if result.status==0:
        class="danger"
        %elif result.status==1:
        class="warning"
        %else:
        class="success"
        %endif
      >
        <td>
          ${result.name}
        </td>
        <td>
          ${result.status}
        </td>
        <td>
          <table class="table table-bordered">
            %for field in result.fields:
            <tr> 
              <td>${field}</td>
              <td>${result.fields[field]}</td>
            </tr>
            %endfor
          </table>
        </td>
      </tr>
    % endfor
    </table>
  </div>
  <div class='col-md-1'></div>
</div>

<div class="row">
  <div class="jumbotron">
    <div class="row">
      <h2>Images:</h2>
    </div>
    <div class="row img-responsive">
      <a href="wires.png">
        <img src="wires.png" class="img-responsive" alt="Image">
      </a>
    </div>
  </div>
</div>

</%block>