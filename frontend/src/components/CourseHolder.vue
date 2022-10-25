<script>

export default {
    props: {
        inCourse: {
            type: Object,
            required: false,
            default: null
        }
    }
    data() {
        return {
            course: this.inCourse
        }
    }
}
</script>