<!-- TODO -->
<h4 class="addon-title">
    {{cookiecutter.full_name}}
</h4>


<div id="{{cookiecutter.short_name}}Scope" class="scripted">
    <!-- Uncomment for debugging. Shows pretty printed ViewModel data -->
    <!-- <pre data-bind="text: ko.toJSON($data, null, 2)"></pre> -->

    <!-- TODO: Settings Interface here -->
    <input data-bind="value: message" type="text" class="form-control">

    <!-- Flashed Messages -->
    <div class="help-block">
        <p data-bind="html: message"></p>
    </div>

</div>
