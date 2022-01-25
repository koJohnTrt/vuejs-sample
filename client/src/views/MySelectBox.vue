<template>
    <div class="m-3">
        <button
            type="button"
            v-if="roadInfos.showButton"
            class="btn btn-primary"
            @click="getRoads()"
        >
            Get Road Data
        </button>
    </div>
    <!-- Main content -->
    <div class="container" v-if="!roadInfos.showButton">
        <h3><i class="fas fa-search"></i> データを選択してください</h3>
        <div class="card" style="background: #d3d3d3">
            <div class="card-body">
                <div class="form-group row">
                    <label for="rec_id" class="col-sm-2 col-form-label">Rec ID</label>
                    <div class="col-sm-6">
                        <Select2 id="rec_id" v-model="recId" :options="roadInfos.rec_ids" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="road_code" class="col-sm-2 col-form-label">Code</label>
                    <div class="col-sm-6">
                        <Select2 id="road_code" v-model="roadCode" :options="roadInfos.codes" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="road_name" class="col-sm-2 col-form-label">Name</label>
                    <div class="col-sm-6">
                        <Select2 id="road_name" v-model="roadName" :options="roadInfos.names" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="date_from" class="col-sm-2 col-form-label">Date From</label>
                    <div class="col-sm-6">
                        <Select2
                            id="date_from"
                            v-model="dateFrom"
                            :options="roadInfos.date_from_data"
                        />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="date_to" class="col-sm-2 col-form-label">Date To</label>
                    <div class="col-sm-6">
                        <Select2 id="date_to" v-model="dateTo" :options="roadInfos.date_to_data" />
                    </div>
                </div>
            </div>
            <!-- /.card-body -->
        </div>
        <!-- /.card -->
        <h3><i class="fas fa-star"></i> 選択されたデータ</h3>
        <pre>
            Rec ID    : {{ recId }}<br />
            Code      : {{ roadCode }} <br />
            Name      : {{ roadName }} <br />
            Date From : {{ dateFrom }} <br />
            Date To   : {{ dateTo }}<br />
        </pre>
    </div>
</template>

<script>
import Select2 from 'vue3-select2-component';
import axios from 'axios';
export default {
    // declare Select2Component
    components: { Select2 },
    data() {
        return {
            recId: '',
            roadCode: '',
            roadName: '',
            dateFrom: '',
            dateTo: '',
            roads: [],
        };
    },
    computed: {
        roadInfos: {
            get() {
                let info = this.roads;
                let rec_ids = [];
                let codes = [];
                let names = [];
                let date_from_data = [];
                let date_to_data = [];
                let showButton = true;

                for (let i in info) {
                    rec_ids.push(info[i].rec_id);
                    codes.push(info[i].code);
                    names.push(info[i].name);
                    date_from_data.push(info[i].date_from);
                    date_to_data.push(info[i].date_to);
                }

                // Get Unique Data
                codes = [...new Set(codes)];
                names = [...new Set(names)];
                date_from_data = [...new Set(date_from_data)];
                date_to_data = [...new Set(date_to_data)];

                if (rec_ids.length) {
                    showButton = false;
                }

                return { rec_ids, codes, names, date_to_data, date_from_data, showButton };
            },
        },
    },
    methods: {
        async getRoads() {
            let { data } = await axios.get('/road_search');
            this.roads = data;
        },
    },
};
</script>
