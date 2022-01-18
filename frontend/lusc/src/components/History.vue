<template>
    <div class="pop">
        <a @click="closePopups()" class="close">
            <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 21 21">
                <path d="M28.5,9.615,26.385,7.5,18,15.885,9.615,7.5,7.5,9.615,15.885,18,7.5,26.385,9.615,28.5,18,20.115,26.385,28.5,28.5,26.385,20.115,18Z" transform="translate(-7.5 -7.5)" fill="#646464"/>
            </svg>
        </a>
        <input v-model="search" type="text" class="search" placeholder="Search"  v-if="focusApp != ''">
        <h3 class="table-title" v-if="focusApp != '' ">{{focusApp}} History</h3>

        <table class="popup-table" v-if="focusApp == 'Luggage'">
            <thead>
                <td>Id</td>
                <td>Luggage</td>
                <td>Size</td>
                <td>Colour</td>
                <td>Date Created</td>
                <td>Deposited</td>
                <td>Date Deposited</td>
                <td>Collected</td>
                <td>Date Collected</td>
            </thead>
            <tbody>
                <tr @click="expandBooking('id')">
                    <td>21045</td>
                    <td>Bucket</td>
                    <td>M</td>
                    <td>Black</td>
                    <td>21 Sep 2021</td>
                    <td>Yes</td>
                    <td>30 Sep 2021</td>
                    <td>No</td>
                    <td>------</td>
                </tr>
            </tbody>
        </table>

        <table class="popup-table" v-else-if="focusApp == 'Transport'">
            <thead>
                <td>Id</td>
                <td>Type</td>
                <td>Destination</td>
                <td>Driver's Name</td>
                <td>Driver's Number</td>
                <td>Vehincle</td>
                <td>Plate Number</td>
                <td>Date Booked</td>
                <td>Approved</td>
            </thead>
            <tbody>
                <tr>
                    <td>21045</td>
                    <td>Private</td>
                    <td>Ilorin</td>
                    <td>John Doe</td>
                    <td>+2348034361009</td>
                    <td>Mercedes(C Class)</td>
                    <td>BV-60-LND</td>
                    <td>30 Sep 2021</td>
                    <td>No</td>
                </tr>
            </tbody>
        </table>

        <table class="popup-table" v-else-if="focusApp == 'Tradefair'">
            <thead>
                <td>Id</td>
                <td>Session</td>
                <td>Semester</td>
                <td>Theme</td>
                <td>Tent</td>
                <td>Date Created</td>
                <td>Total Amount (₦)</td>
                <td>Approved</td>
            </thead>
            <tbody>
                <tr>
                    <td>21045</td>
                    <td>2021</td>
                    <td>Omega</td>
                    <td>Prison Break</td>
                    <td>Full</td>
                    <td>25 Sep 2021</td>
                    <td>5 000.00</td>
                    <td>No</td>
                </tr>
            </tbody>
        </table>

        <div class="else" v-else>
            <span class="extra">🤕</span><br>Ooops,<br>This was not supposed to happen...<br> Check back later.
        </div>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'

export default {
    setup () {
        const state = reactive({
            count: 0,
        })

        function expandBooking(id) {
            alert(id)
        }

        function closeBooking() {
            alert("booking closed")
        }
    
        return {
            ...toRefs(state),
            expandBooking,
            closeBooking,
        }
    }
}
</script>

<style lang="css" scoped>

</style>